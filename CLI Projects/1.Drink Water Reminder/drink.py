import notifypy


def main():
    notification = notifypy.Notify(default_notification_application_name="Python Application (drink.py)")
    notification.title = "Time To Drink Water"
    notification.message = "Fill your glass if empty\nand drink 1 glass of water"
    notification.icon = "Glass of Water Icon.jfif"
    notification.send()


# This script will only run if the main function is called, and the main function will only be called if the file is
#   run from here
# If this file is imported in another file then the main function
#   will not be called
if __name__ == "__main__":
    main()
