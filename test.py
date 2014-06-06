from observers import observers

import unittest

class test_observers(unittest.TestCase):

    def test_create(self):
        obs = observers()
        self.assertTrue(isinstance(obs, observers))


class test_register(unittest.TestCase):
    def setUp(self):
        self.called = 0
        self.called_2 = 0
        self.calling_kw = None
        self.calling_args = None
        self.obs = observers()
        self.obs.register(self.listener, 'topic')

    def listener(self, *args, **kw):
        self.called += 1
        self.calling_args = args
        self.calling_kw = kw

    def listener_2(self):
        self.called_2 += 1

    def test_registry(self):
        self.assertTrue(self.listener in self.obs.registered('topic'))

    def test_registry_2(self):
        self.obs.register(self.listener, 'topic')
        self.assertEqual(len(self.obs.registered('topic')), 1)

    def test_notify(self):
        self.obs.notify('topic')
        self.assertEqual(self.called, 1)
        
    def test_notify_correct(self):
        self.obs.register(self.listener_2, 'topic_2')
        self.obs.notify('topic_2')
        self.assertEqual(self.called, 0, 'topic failed')
        self.assertEqual(self.called_2, 1, 'topic 2 failed')

    def test_notify_2(self):
        self.obs.register(self.listener, 'topic_2')
        self.obs.notify('topic_2')
        self.assertEqual(self.called, 1, 'topic failed')
        self.assertEqual(self.called_2, 0, 'topic 2 failed')
        self.obs.notify('topic')
        self.assertEqual(self.called, 2, 'topic failed')
        self.assertEqual(self.called_2, 0, 'topic 2 failed')
    
    def test_notify_kw(self):
        self.obs.notify('topic', fred=1, tom=2)
        self.assertEqual(self.calling_kw, dict(fred=1, tom=2))
        self.assertEqual(self.calling_args, ())

    def test_notify_args(self):
        self.obs.notify('topic', 1, 2)
        self.assertEqual(self.calling_kw, dict())
        self.assertEqual(self.calling_args, (1, 2))



