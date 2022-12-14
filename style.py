style = ('''
/* Widget */

QWidget{
    background-color : #EDEDED;
}

/* Menu */

QMenu {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
}

QMenu::item:selected {
    background-color : #18a6de;
    color            : white;
    border-radius    : 2px;
}

/* MenuBar */

QMenuBar::item {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
}

QMenuBar::item:selected {
    background-color : #18a6de;
    color            : white;
    border           : 2px solid white;
}

/* PushButton */

QPushButton {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QPushButton:hover {
    background-color : #18a6de;
    color            : white;
    border           : 2px solid white;
}

QPushButton:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
    border-radius    : 4px;
}

/* TextBrowser */

QTextBrowser {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QTextBrowser:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
    border-radius    : 4px;
}

/* TextEdit */

QTextEdit {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QTextEdit:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
    border-radius    : 4px;
}

QListWidget {
    font-size: 12pt;
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QListWidget:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
    border-radius    : 4px;
}

/* LineEdit */

QLineEdit {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QLineEdit:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
    border-radius    : 4px;
}

/* SpinBox */

QSpinBox {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
}

QSpinBox:disabled {
    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
}

/* ComboBox */

QComboBox {
    padding          : 1px 0px 1px 3px;
    font-size: 11pt;

    background-color : white;
    color            : black;
    border           : 2px solid #18a6de;
}

QComboBox:hover {
    padding          : 1px 0px 1px 3px;

    background-color : #18a6de;
    color            : black;
    border           : 2px solid white;
}

QComboBox:disabled {
    padding          : 1px 0px 1px 3px;

    background-color : white;
    color            : #9ea2a3;
    border           : 2px solid #93bccc;
}

QComboBox QAbstractItemView {
    background-color : white;
    color            : black;
    border           : 2px solid #18a6de
}

QComboBox::down-arrow {
    padding-right : 5px;
    border-image  : url(Resourses/arrow_down.png);
}

/* QCheckBox */

QCheckBox::indicator::unchecked {
    background-color : white;
    border           : 2px solid #18a6de;
    border-radius    : 4px;
}

QCheckBox::indicator::checked {
    background-color : #18a6de;
    border           : 2px solid white;
    border-radius    : 4px;
}

QCheckBox::indicator::checked::hover {
    background-color                       : #1bbbfa;
    border: 2px solid white; border-radius : 4px;
}

QCheckBox::indicator::unchecked::hover {
    background-color                        : white;
    border: 2px solid #1bbbfa;border-radius : 4px;
}

QCheckBox::indicator::checked:pressed {
    background-color : #ebf9ff;
    border           : 2px solid #5acdfa;
    border-radius    : 4px;
}

QCheckBox::indicator::unchecked:pressed {
    background-color : #5acdfa;
    border           : 2px solid #ebf9ff;
    border-radius    : 4px;
}

/* RadioButton */

QRadioButton::indicator::unchecked {
    background-color : white;
    border           : 2px solid #18a6de;
    border-radius    : 6px;
}

QRadioButton::indicator::checked {
    background-color : #18a6de;
    border           : 2px solid white;
    border-radius    : 6px;
}

QRadioButton::indicator::checked::hover {
    background-color                       : #1bbbfa;
    border: 2px solid white; border-radius : 6px;
}

QRadioButton::indicator::unchecked::hover {
    background-color                        : white;
    border: 2px solid #1bbbfa;border-radius : 6px;
}

QRadioButton::indicator::checked:pressed {
    background-color : #ebf9ff;
    border           : 2px solid #5acdfa;
    border-radius    : 6px;
}

QRadioButton::indicator::unchecked:pressed {
    background-color : #5acdfa;
    border           : 2px solid #ebf9ff;
    border-radius    : 6px;
}
''')