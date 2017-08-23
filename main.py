import sys
from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1080
        self.height = 960
        self.widget = qlWidget(self)
        self.button = QPushButton('Test', self)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.widget)
        mainLayout.addWidget(self.button)

        # Button action
        self.button.clicked.connect(self.widget.initializeGL)

        self.setLayout(mainLayout)
        self.initUI()

    # Move window to middle of the screen
    def setMiddle(self):
        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        y = screen.height() - widget.height()
        self.move(x, y)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        self.setMiddle()

class qlWidget(QGLWidget):

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        #self.setMaximumSize(640,480)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -6.0)
        glColor3f( 1.0, 1.5, 0.0 );
        glPolygonMode(GL_FRONT, GL_FILL);

        glBegin(GL_TRIANGLES)
        glVertex3f(0.0,0.5,0.0)
        glVertex3f(0.5,-0.5,0.0)
        glVertex3f(-0.5,-0.5,0.0)
        glEnd()

        glFlush()


    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.33, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())