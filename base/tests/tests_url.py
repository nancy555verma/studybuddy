from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import loginPage, logoutUser, registerPage, home, room, userProfile, \
    createRoom, updateRoom, deleteRoom, deleteMessage, updateUser, topicsPage, activitiesPage

from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logoutUser)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerPage)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_room_url_is_resolved(self):
        url = reverse('room', args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, room)

    def test_userprofile_url_is_resolved(self):
        url = reverse('user-profile', args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, userProfile)

    def test_create_room_url_is_resolved(self):
        url = reverse('create-room')
        print(resolve(url))
        self.assertEquals(resolve(url).func, createRoom)

    def test_update_room_url_is_resolved(self):
        url = reverse('update-room', args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateRoom)

    def test_delete_room_url_is_resolved(self):
        url = reverse('delete-room', args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, deleteRoom)

    def test_delete_message_url_is_resolved(self):
        url = reverse('delete-message', args=['id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, deleteMessage)

    def test_update_user_url_is_resolved(self):
        url = reverse('update-user')
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateUser)

    def test_topics_url_is_resolved(self):
        url = reverse('topics')
        print(resolve(url))
        self.assertEquals(resolve(url).func, topicsPage)

    def test_activities_url_is_resolved(self):
        url = reverse('activities')
        print(resolve(url))
        self.assertEquals(resolve(url).func, activitiesPage)

    # urls with class based views

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetView)

    def test_password_reset_confirm_url_is_resolved(self):
        url = reverse('password_reset_confirm', args=['uid', 'token'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)
