from abc import ABC, abstractmethod
# -------------------------------------------------------------------------------------------------------------------
# This program demonstrates the adherence to SOLID principles in the design of a fitness tracker system.

# Single Responsibility Principle (SRP):
# Each class in this program has a single responsibility, ensuring that it has only one reason to change.
# - User class focuses on representing user-related information.
# - Activity and its subclasses focus on defining activities and processing activity data.
# - ActivityMonitor class handles monitoring activities and notifying displays.
# - DataStorage class focuses on saving data.
# - Display class focuses on displaying activity data.

# Open-Closed Principle (OCP):
# The Observer pattern is leveraged in the ActivityMonitor class, allowing the addition of new activity types
# without modifying existing code. The Display can be extended for new activity types.

# Liskov Substitution Principle (LSP):
# The Activity class and its subclasses adhere to the contracts of the Observer pattern.
# They implement the 'update' method, making them compatible with the notification mechanism in ActivityMonitor.

# Interface Segregation Principle (ISP):
# While separate interfaces for data collection and display are not explicitly defined in this code,
# the Activity class and its subclasses implicitly follow the notification contracts required for observing activities.

# Dependency Inversion Principle (DIP):
# Dependencies like DataStorage and Display are injected into the ActivityMonitor constructor,
# following DIP to achieve loose coupling and facilitate easier testing.

# The overall design ensures modularity, extensibility, and testability, aligning with SOLID principles.
# -------------------------------------------------------------------------------------------------------------------

# Represents a user with attributes like name and age.
# Adheres to Single Responsibility Principle (SRP) by focusing on user-related information.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Abstract base class representing different activities like walking, running, swimming, cycling, etc.
# Adheres to Liskov Substitution Principle (LSP) by ensuring compatibility with the Observer pattern.
class Activity(ABC):
    @abstractmethod
    def update(self, data):
        pass

# Concrete class representing walking activity.
# Implements the 'update' method to process walking data.
# Adheres to LSP by fulfilling the contracts of the Observer pattern.
class Walking(Activity):
    def update(self, data):
        print(f"Processing walking data: {data}")

# This class monitors user activities and notifies observers (Display) when new data is collected.
# Adheres to Open-Closed Principle (OCP) by allowing the addition of new activity types without modifying existing code.
# Adheres to Dependency Inversion Principle (DIP) by injecting dependencies like DataStorage and Display.
class ActivityMonitor:
    def __init__(self, user, data_storage, display):
        self.user = user
        self.data_storage = data_storage
        self.display = display
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.notify_display(activity)
        print(f"Added {activity.__class__.__name__} to activities.")

    def notify_display(self, activity):
        # Notify observers (Display) about the new activity
        self.display.notify(activity)

# Class responsible for saving user activity data.
# Adheres to SRP by focusing on storing data.
class DataStorage:
    def save_data(self, data):
        print(f"Saving data: {data}")

# Class responsible for displaying user activity data.
# Adheres to SRP by focusing on displaying data.
class Display:
    def notify(self, activity):
        print(f"Notifying display about {activity.__class__.__name__} data.")

def main():
    # Dummy data
    user = User(name="Jane Doe", age=30)
    data_storage = DataStorage()
    display = Display()
    
    # Create an ActivityMonitor and inject dependencies for loose coupling and easier testing.
    monitor = ActivityMonitor(user, data_storage, display)

    walking_activity = Walking()
    monitor.add_activity(walking_activity)

if __name__ == "__main__":
    main()
