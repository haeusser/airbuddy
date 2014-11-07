__author__ = 'Philip'

from TravelCase import TravelCase

# query db for cases
cases = db.Query(TravelCase).run()  # TODO: select where date=today

# for debugging purposes, print cases
for c in cases:
  print str(c.firstname)

# TODO check, if flight arrives today

    # TODO check status

    # TODO status changed? --> email

    # TODO landing in <2h --> email