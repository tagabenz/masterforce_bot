import unittest
import start


class TestCase( unittest.TestCase ):
    def setUp( self ):
        start.app.config["TESTING"] = True
        self.app = start.app.test_client()

    def test_get_mainpage( self ):
        page = self.app.post( "/index", data=dict(name="Moby Dick") )
        assert page.status_code == 200
        assert 'Moby Dick' in str( page.data )

    def test_html_escaping( self ):
        page = self.app.post( "/index", data=dict(name='"><b>TEST</b><!--') )
        assert '<b>' not in str( page.data )


if __name__ == '__main__':
    unittest.main()
