from django.test import TestCase
from account import models as amod
from lxml import etree
from datetime import datetime
from django.contrib.auth import models as pmod

class MyTests(TestCase):
    fixtures = ['account.yaml']

    def setUp(self):
        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer"
        self.homer.last_name = "Simpson"
        self.homer.birthdate = datetime(2000, 1, 1)
        self.homer.save()

    def test_user_get(self):
        u1 = amod.User.objects.get(pk=3)
        self.assertEqual(u1.username, 'mcrofts6', msg="username should be mcrofts6")

    def test_create_user(self):
        amod.User.objects.create_user(username='taylor', password='password', first_name='Taylor', last_name='Crofts', email='taylor@taylor.com').save()
        test_user = amod.User.objects.get(username='taylor')
        self.assertEqual(test_user.username, 'taylor')
        self.assertEqual(test_user.first_name, 'Taylor')
        self.assertEqual(test_user.last_name, 'Crofts')
        self.assertEqual(test_user.email, 'taylor@taylor.com')

    def test_update_password(self):
        amod.User.objects.create_user(username='taylor', password='password', first_name='Taylor', last_name='Crofts', email='taylor@taylor.com').save()
        test_user = amod.User.objects.get(username='taylor')
        self.assertEquals(test_user.check_password('password'), True)

        test_user.set_password('new_password')
        test_user.save()
        self.assertEquals(test_user.check_password('new_password'), True)

    def test_user_login(self):
        credentials = {
            'username': 'mcrofts6',
            'password': 'password'
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        print(request.user.username)
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.username, 'mcrofts6', msg="User should have been homer")
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def test_user_groups(self):
        #Add new group to db with user some persmissions
        test_group = pmod.Group() 
        test_group.name = "Admin"
        test_group.save()
        test_group.permissions.add(pmod.Permission.objects.get(codename='add_user'))
        test_group.permissions.add(pmod.Permission.objects.get(codename='delete_user'))
        test_group.permissions.add(pmod.Permission.objects.get(codename='change_user'))
        test_group.save()

        #Add user to group
        self.homer.groups.add(test_group)

        #Check to see if user now has permissions from test_group
        self.assertTrue(self.homer.has_perm('account.add_user'), msg="No permission for add_user")
        self.assertTrue(self.homer.has_perm('account.delete_user'), msg="No permission for delete_user")
        self.assertTrue(self.homer.has_perm('account.change_user'), msg="No permission for change_user")

    def test_user_permissions(self):
        #Create a new permission
        test_permission = pmod.Permission(name='testing persmission', codename='test', content_type=pmod.Permission.objects.get(codename='add_user').content_type)
        test_permission.save()

        #Give user new permission
        self.homer.user_permissions.add(test_permission)

        #Check to see if user has permission
        self.assertTrue(self.homer.has_perm('account.test'), msg="Persmission test was not added to user")