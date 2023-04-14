class Tag:
    __name: str = ""
    __description: str = ""

    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name
    
    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description


class Chat:
    logs: dict[int, list[str]] = None

    def __init__(self) -> None:
        pass

    def add_user(self, user_id) -> None:
        self.logs[user_id] = []

    def add_message(self, user_id, message: str) -> None:
        self.logs[user_id].append(message)

    def get_logs(self) -> dict[int, list[str]]:
        return self.logs


class Calendar:
    reminders: dict[str, list[str]]

    def __init__(self) -> None:
        pass

    def get_reminders(self) -> dict[str, list[str]]:
        return self.reminders

    def add_reminder(self, date: str, reminder: str) -> None:
        self.reminders[date] = [reminder]

    def remove_reminders(self, date: str) -> None:
        del self.reminders[date]


class User:
    __name: str
    __id: int
    __interests: list[Tag]

    def __init__(self, name: str, id: int) -> None:
        self.__name = name
        self.__id = id


    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_interests(self) -> list[Tag]:
        return self.__interests

    def add_interest(self, interest: Tag) -> None:
        self.__interests.append(interest)


class Club:
    __name: str
    __description: str
    __users: list[User]
    __members: int
    __setting: str
    __tags: list[Tag]
    __chat: Chat
    __calendar: Calendar


    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str) -> None:
        self.__description = description

    def get_users(self) -> list[User]:
        return self.__users

    def add_user(self, user: User) -> None:
        self.__users.append(user)

    def get_members(self) -> int:
        return self.__members

    def inc_members(self) -> None:
        self.__members += 1

    def dec_members(self) -> None:
        self.__members -= 1

    def get_setting(self) -> str:
        return self.__setting

    def set_setting(self, setting: str) -> None:
        self.__setting = setting

    def get_tags(self) -> list[Tag]:
        return self.__tags

    def add_tags(self, tag: Tag) -> None:
        self.__tags.append(tag)

    def get_chat(self) -> Chat:
        return self.__chat

    def get_calendar(self) -> Calendar:
        return self.__calendar