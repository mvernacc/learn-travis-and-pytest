from distutils.core import setup

INSTALL_REQUIRES = []
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
]

setup(
    name='learn-travis-and-pytest',
    packages=['woowaa'],
    version='0.0.1',
    description='Test project to get acquainted with TravisCI',
    url='https://github.com/mvernacc/learn-travis-and-pytest',
    extras_require={
    	'test': TEST_REQUIRES + INSTALL_REQUIRES,
    }
)
