import pytest

from test_api.base_service import BaseService

DOMAIN = "http://localhost:8000"


class TmsService(BaseService):

    def login(self, email, password):
        """
        User/Admin authentication
        :param email
        :param password
        :return: dict с access_token
        """
        url = f"{DOMAIN}/auth/login"
        body = {"email": email, "password": password}
        # For login you don`t need token, so give None
        response = self.post(url, token=pytest.token, body=body, code=200)
        return response

    def register_admin(self, username, email, password, code=None):
        """
        Admin registration
        :param username
        :param email
        :param password
        :param code
        :return: server response
        """
        url = f"{DOMAIN}/auth/register-admin"
        body = {"username": username, "email": email, "password": password}
        response = self.post(url, token=pytest.token, body=body, code=code)
        return response

    def create_board(self, title, description, public):
        """
        Board creation
        :param title: Name of the board
        :param description: description of the board
        :param public: is the board public(bool)
        :return: server response with the data created board
        """
        url = f"{DOMAIN}/boards"
        body = {"title": title, "description": description, "public": public}
        # Token is got from pytest.token automatically
        response = self.post(url, token=pytest.token, body=body, code=201)
        return response

    def create_task(self, board_id, title, description, status, priority):
        """
        Task creation
        :param board_id:
        :param title:
        :param description:
        :param status:
        :param priority:
        :return:
        """
        url = f"{DOMAIN}/boards/{board_id}/tasks"
        body = {
            "title": title,
            "description": description,
            "status": status,
            "priority": priority,
        }
        response = self.post(url, token=pytest.token, body=body, code=201)
        return response

    def get_users(self, skip=0, limit=100, code=200):
        """
        Get users list
        :param skip: amount of users to skip
        :param limit: maximum number of users to fetch
        :param code: expected HTTP code
        :return: users list
        """
        url = f"{DOMAIN}/users/?skip={skip}&limit={limit}"
        response = self.get(url, token=pytest.token, code=code)
        return response

    def get_board_members(self, board_id, code=200):
        """
        Get list of boards members
        :param board_id:
        :param code:
        :return: list of boards members
        """
        url = f"{DOMAIN}/boards/{board_id}/members"
        response = self.get(url, token=pytest.token, code=code)
        return response

    def add_board_member(self, board_id, user_id, code=200):
        """
        Adding board member
        :param board_id:
        :param user_id:
        :param code:
        :return: server response
        """
        url = f"{DOMAIN}/boards/{board_id}/members/{user_id}"
        response = self.post(url, token=pytest.token, code=code)
        return response

    def task_next_status(self, task_id, code=200):
        """
        Task next status
        :param task_id:
        :param code:
        :return: updated task
        """
        url = f"{DOMAIN}/tasks/{task_id}/next-status"
        response = self.put(url, token=pytest.token, body=None, code=code)
        return response

    def update_task_status(self, board_id, task_ids, new_status, code=200):
        """
        Update task status
        :param board_id: ID of board
        :param task_ids: list of ID tasks
        :param new_status: new status
        :param code: expected HTTP code
        :return: server response
        """
        url = f"{DOMAIN}/boards/{board_id}tasks/{task_ids}/bulk/status"
        body = {"task_ids": task_ids, "new_status": new_status}
        response = self.put(url, token=pytest.token, body=body, code=code)
        return response

    def get_board_stats(self, board_id, code=200):
        """
        Get board stats
        :param board_id:
        :param code:
        :return:
        """
        url = f"{DOMAIN}/boards/{board_id}/stats"
        response = self.get(url, token=pytest.token, code=code)
        return response

    def search_tasks(self, query, skip=0, limit=100, code=200):
        """
        Search tasks
        :param query:
        :param skip:
        :param limit:
        :param code:
        :return: list of found tasks
        """
        url = f"{DOMAIN}/tasks/?search={query}&skip={skip}&limit={limit}"
        response = self.get(url, token=pytest.token, code=code)
        return response

    def update_task_priority(self, task_id, priority, code=200):
        """
        Update task priority
        :param task_id:
        :param priority:
        :param code:
        :return:
        """
        url = f"{DOMAIN}/tasks/{task_id}/priority/{priority}"
        response = self.put(url, token=pytest.token, body=None, code=code)
        return response

    def get_my_tasks(self, skip=0, limit=100, code=200):
        """
        Get my tasks
        :param skip:
        :param limit:
        :param code:
        :return:
        """
        url = f"{DOMAIN}/users/me/tasks?search={skip}&limit={limit}"
        response = self.get(url, token=pytest.token, code=code)
        return response

    def archive_board(self, board_id, code=200):
        """
        Archive board
        :param board_id:
        :param code:
        :return:
        """
        url = f"{DOMAIN}/boards/{board_id}/archive"
        response = self.put(url, token=pytest.token, body=None, code=code)
        return response

    def moving_tasks(self, task_id, target_board_id, code=200):
        """
        Moving tasks
        :param task_id:
        :param target_board_id:
        :param code:
        :return:
        """
        url = f"{DOMAIN}/tasks/{task_id}/move-to/{target_board_id}"
        response = self.put(url, token=pytest.token, body=None, code=code)
        return response
