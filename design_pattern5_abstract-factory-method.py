# Abstract Factory Design Pattern
"""
Abstract Factory is a creational design pattern that provides an interface for creating families of related objects without specifying
their concrete classes. It is useful when you need multiple related objects that should work together.

| Factory Method             | Abstract Factory                     |
| -------------------------- | ------------------------------------ |
| Creates one product        | Creates a family of related products |
| Focuses on a single object | Focuses on groups of objects         |
| Simpler                    | More scalable                        |

the key idea is:"Create related objects together through a family-specific factory."

Example: You have a GUI application.

Windows Factory creates:

Windows Button
Windows Checkbox

Mac Factory creates:

Mac Button
Mac Checkbox

The client only asks the factory, not the specific classes.

Abstract Factory is a creational design pattern that provides an interface to create families of related objects without specifying their concrete classes.

Factory Method  -> One product
Abstract Factory -> Family of products

EmailFactory:
   -> EmailSender
   -> EmailTemplate

SMSFactory:
   -> SMSSender
   -> SMSTemplate


"""

class WindowsFactory:
    def create_button(self):
        return "Windows Button"

    def create_checkbox(self):
        return "Windows Checkbox"


class MacFactory:
    def create_button(self):
        return "Mac Button"

    def create_checkbox(self):
        return "Mac Checkbox"


# Client Code
factory = WindowsFactory()

print(factory.create_button())
print(factory.create_checkbox())


"""
A real-world Abstract Factory example is a Notification System.

You can send notifications through:

Email
SMS

Each type needs 2 related objects:

Sender
Template

"""

from abc import ABC, abstractmethod

class NotificationFactory(ABC):

    @abstractmethod
    def create_sender(self):
        pass

    @abstractmethod
    def create_template(self):
        pass


class EmailFactory(NotificationFactory):

    def create_sender(self):
        return "Email Sender"

    def create_template(self):
        return "Email Template"

class SMSFactory(NotificationFactory):

    def create_sender(self):
        return "SMS Sender"

    def create_template(self):
        return "SMS Template"

factory = EmailFactory()

print(factory.create_sender())
print(factory.create_template())

"""
| Factory      | Object 1    | Object 2      |
| ------------ | ----------- | ------------- |
| EmailFactory | EmailSender | EmailTemplate |
| SMSFactory   | SMSSender   | SMSTemplate   |

"""
