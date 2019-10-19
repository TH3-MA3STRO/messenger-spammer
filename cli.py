from pyfiglet import Figlet
import platform
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

f = Figlet(font='slant', width=57)
print(f.renderText('messenger spammer'))


def print_r(sys):
    print('''
********************************************************
*                                                      *
*    Author: TH3-MA3STRO                               *
*    Instagtam: @th3_ma3stro                           *
*    GitHub: https://www.github.com/TH3-MA3STRO        *
*    Platform: {}                                 *
*                                                      *
********************************************************
    '''.format(sys))


if platform.system().lower() == 'linux':
    print_r('Linux  ')
elif platform.system().lower() == 'windows':
    print_r('Windows')


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end
        if not int(document.text) <= 50:
            raise ValidationError(
                message="Please enter a number  <= 50",
                cursor_position=len(document.text))


def styler():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#ff1f17',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '#f44336 bold',  # default
        Token.Answer: '#ccf5ff',
        Token.Question: '#21ed39',
    })
    return style


def spam_info():
    questions = [
        {
            'type': 'input',
            'message': 'Enter spam receiver:',
            'name': 'contact',
        },
        {
            'type': 'input',
            'message': 'Enter the message you wish to spam:',
            'name':'msg'
        },
        {
            'type': 'input',
            'message': 'Enter the count of messages:',
            'name': 'count',
            'validate': NumberValidator
        }
    ]
    answers = prompt(questions, style=styler())
    return answers


def login_info():
    questions = [
        {
            'type': 'input',
            'message': "Enter your E-Mail or Phone:",
            'name': 'username'
        },
        {
            'type': 'password',
            'message': "Enter your password:",
            'name': 'password'
        }
    ]

    answers = prompt(questions, style=styler())
    return answers
