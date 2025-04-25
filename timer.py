import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QWidget, QSpinBox, QDialog,
                            QGridLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class CountdownDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('设置倒计时时间')
        self.setStyleSheet("background-color: rgba(30, 30, 30, 220); color: white;")
        
        layout = QGridLayout()
        
        # 时分秒设置
        self.hours_spin = QSpinBox()
        self.hours_spin.setRange(0, 99)
        self.hours_spin.setStyleSheet("background-color: rgba(60, 60, 60, 220); color: white;")
        
        self.minutes_spin = QSpinBox()
        self.minutes_spin.setRange(0, 59)
        self.minutes_spin.setStyleSheet("background-color: rgba(60, 60, 60, 220); color: white;")
        
        self.seconds_spin = QSpinBox()
        self.seconds_spin.setRange(0, 59)
        self.seconds_spin.setStyleSheet("background-color: rgba(60, 60, 60, 220); color: white;")
        
        layout.addWidget(QLabel('时:'), 0, 0)
        layout.addWidget(self.hours_spin, 0, 1)
        layout.addWidget(QLabel('分:'), 0, 2)
        layout.addWidget(self.minutes_spin, 0, 3)
        layout.addWidget(QLabel('秒:'), 0, 4)
        layout.addWidget(self.seconds_spin, 0, 5)
        
        # 确认和取消按钮
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton('确认')
        self.confirm_button.setStyleSheet("background-color: rgba(60, 60, 60, 220); color: white;")
        self.confirm_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton('取消')
        self.cancel_button.setStyleSheet("background-color: rgba(60, 60, 60, 220); color: white;")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout, 1, 0, 1, 6)
        
        self.setLayout(layout)
    
    def get_time(self):
        return self.hours_spin.value(), self.minutes_spin.value(), self.seconds_spin.value()

class TransparentTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.running = False
        self.mode = "正计时"  # 默认为正计时模式
        
    def initUI(self):
        # 设置窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.FramelessWindowHint |      # 无边框
            Qt.WindowStaysOnTopHint |     # 窗口置顶
            Qt.Tool                       # 工具窗口，不在任务栏显示
        )
        
        # 主布局
        main_widget = QWidget()
        main_widget.setAttribute(Qt.WA_TranslucentBackground)
        main_layout = QVBoxLayout(main_widget)
        
        # 计时器标签
        self.time_label = QLabel("00:00:00")
        self.time_label.setFont(QFont('Arial', 24))
        self.time_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 120); border-radius: 10px; padding: 10px;")
        self.time_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.time_label)
        
        # 模式标签
        self.mode_label = QLabel("正计时模式")
        self.mode_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 120); border-radius: 5px; padding: 2px;")
        self.mode_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.mode_label)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        
        # 开始/暂停按钮
        self.start_pause_button = QPushButton("开始")
        self.start_pause_button.setStyleSheet("background-color: rgba(60, 60, 60, 180); color: white; border-radius: 5px;")
        self.start_pause_button.clicked.connect(self.toggle_timer)
        button_layout.addWidget(self.start_pause_button)
        
        # 重置按钮
        self.reset_button = QPushButton("重置")
        self.reset_button.setStyleSheet("background-color: rgba(60, 60, 60, 180); color: white; border-radius: 5px;")
        self.reset_button.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_button)
        
        # 切换模式按钮
        self.switch_mode_button = QPushButton("切换为倒计时")
        self.switch_mode_button.setStyleSheet("background-color: rgba(60, 60, 60, 180); color: white; border-radius: 5px;")
        self.switch_mode_button.clicked.connect(self.switch_mode)
        button_layout.addWidget(self.switch_mode_button)
        
        # 退出按钮
        self.exit_button = QPushButton("退出")
        self.exit_button.setStyleSheet("background-color: rgba(60, 60, 60, 180); color: white; border-radius: 5px;")
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.exit_button)
        
        main_layout.addLayout(button_layout)
        
        self.setCentralWidget(main_widget)
        
        # 设置定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.setInterval(1000)  # 每秒更新一次
        
        # 设置窗口大小和位置
        self.resize(400, 130)
        self.center()
        self.setWindowTitle('多功能计时器')
        
    def center(self):
        # 将窗口居中显示
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))
    
    def toggle_timer(self):
        if not self.running:
            self.timer.start()
            self.running = True
            self.start_pause_button.setText("暂停")
        else:
            self.timer.stop()
            self.running = False
            self.start_pause_button.setText("继续")
    
    def reset_timer(self):
        self.timer.stop()
        self.running = False
        
        if self.mode == "正计时":
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.time_label.setText("00:00:00")
        else:
            self.show_countdown_dialog()
            
        self.start_pause_button.setText("开始")
    
    def update_time(self):
        if self.mode == "正计时":
            self.seconds += 1
            
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
        else:  # 倒计时模式
            if self.seconds > 0:
                self.seconds -= 1
            elif self.minutes > 0:
                self.minutes -= 1
                self.seconds = 59
            elif self.hours > 0:
                self.hours -= 1
                self.minutes = 59
                self.seconds = 59
            else:
                # 倒计时结束
                self.timer.stop()
                self.running = False
                self.time_label.setStyleSheet("color: red; background-color: rgba(0, 0, 0, 120); border-radius: 10px; padding: 10px;")
                self.start_pause_button.setText("开始")
                return
        
        time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.time_label.setText(time_str)
    
    def switch_mode(self):
        self.timer.stop()
        self.running = False
        
        if self.mode == "正计时":
            self.mode = "倒计时"
            self.mode_label.setText("倒计时模式")
            self.switch_mode_button.setText("切换为正计时")
            self.show_countdown_dialog()
        else:
            self.mode = "正计时"
            self.mode_label.setText("正计时模式")
            self.switch_mode_button.setText("切换为倒计时")
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.time_label.setText("00:00:00")
            self.time_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 120); border-radius: 10px; padding: 10px;")
        
        self.start_pause_button.setText("开始")
    
    def show_countdown_dialog(self):
        dialog = CountdownDialog(self)
        if dialog.exec_():
            self.hours, self.minutes, self.seconds = dialog.get_time()
            time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.time_label.setText(time_str)
            self.time_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 120); border-radius: 10px; padding: 10px;")
    
    # 实现鼠标拖动功能
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

def main():
    app = QApplication(sys.argv)
    timer = TransparentTimer()
    timer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()