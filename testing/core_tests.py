from core import User, Club, Tag, Chat, Calendar

class CoreTests:

    def test_tag(self):
        tag = Tag("test_tag", "A test decscription")

        assert tag.get_name() == "test_tag"
        assert tag.get_description() == "A test decscription"
        tag.set_name("new_name")
        assert tag.get_name() == "new_name"
        tag.set_description("A new description")
        assert tag.get_description() == "A new description"

    def test_chat(self):
        chat = Chat()

        chat.add_user(1)
        chat.add_message(1, "Test message 1")
        chat.add_message(1, "Test message 2")
        chat.add_user(2)
        chat.add_message(2, "Test message 3")
        logs = chat.get_logs()
        assert logs == {1: ["Test message 1", "Test message 2"], 2: ["Test message 3"]}


    def test_calendar(self):
        calendar = Calendar()

        calendar.add_reminder("2023-04-20", "Test reminder 1")
        calendar.add_reminder("2023-04-20", "Test reminder 2")
        calendar.add_reminder("2023-04-21", "Test reminder 3")
        reminders = calendar.get_reminders()
        assert reminders == {"2023-04-20": ["Test reminder 1", "Test reminder 2"],"2023-04-21": ["Test reminder 3"],}

        calendar.remove_reminders("2023-04-20")
        reminders = calendar.get_reminders()
        assert reminders == {"2023-04-21": ["Test reminder 3"]}

    def test_user(self):
        user = User("Test user", 1)

        assert user.get_name() == "Test user"
        assert user.get_id() == 1
        user.set_name("New name")
        assert user.get_name() == "New name"

        tag1 = Tag("tag1", "Tag 1 description")
        tag2 = Tag("tag2", "Tag 2 description")

        user.add_interest(tag1)
        user.add_interest(tag2)
        interests = user.get_interests()
        assert interests == [tag1, tag2]

    def test_club(self):
        tag1 = Tag("tag1", "Tag 1 description")
        tag2 = Tag("tag2", "Tag 2 description")
        tag3 = Tag("tag3", "Tag 3 description")

        user1 = User("Alice", 1)
        user2 = User("Bob", 2)
        user3 = User("Charlie", 3)

        club = Club("My Club", "Setting")

        assert club.get_name() == "My Club"
        club.set_name("New Club Name")
        assert club.get_name() == "New Club Name"
        assert club.get_description() == ""
        club.set_description("New Club Description")
        assert club.get_description() == "New Club Description"
        assert club.get_users() == []
        club.add_user(user1)
        assert club.get_users() == [user1]
        club.add_user(user2)
        club.add_user(user3)
        assert club.get_users() == [user1, user2, user3]
        assert club.get_members() == 0
        club.inc_members()
        assert club.get_members() == 1
        club.dec_members()
        assert club.get_members() == 0
        assert club.get_setting() == "Setting"
        club.set_setting("New Setting")
        assert club.get_setting() == "New Setting"
        assert club.get_tags() == []
        club.add_tags(tag1)
        assert club.get_tags() == [tag1]
        club.add_tags(tag2)
        club.add_tags(tag3)
        assert club.get_tags() == [tag1, tag2, tag3]
        assert isinstance(club.get_chat(), Chat)
        assert isinstance(club.get_calendar(), Calendar)
        assert len(club.get_users()) == 3
        club.get_users().remove(user1)
        assert len(club.get_users()) == 2
        assert len(club.get_tags()) == 3
        club.get_tags().remove(tag1)
        assert len(club.get_tags()) == 2

        club.get_chat().add_user(1)
        club.get_chat().add_message(1, "Hello, World!")
        assert club.get_chat().get_logs() == {1: ["Hello, World!"]}
        club.get_chat().add_user(2)
        club.get_chat().add_message(2, "Hi, there!")
        assert club.get_chat().get_logs() == {1: ["Hello, World!"], 2: ["Hi, there!"]}
        club.get_chat().add_message(1, "How are you?")
        assert club.get_chat().get_logs() == {1: ["Hello, World!", "How are you?"], 2: ["Hi, there!"]}

    def call_tests(self):
        self.test_tag()
        self.test_chat()
        self.test_calendar()
        self.test_user()
        self.test_club()

        print("All tests passed!")


tests = CoreTests()
tests.call_tests()

