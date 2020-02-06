from __future__ import unicode_literals
import argparse
import csv

import transaction
from pyramid.paster import bootstrap

from voteit.irl.models.interfaces import IParticipantNumbers
from voteit.irl.models.participant_numbers import ParticipantNumberTicket


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_uri", help="Paster ini file to load settings from")
    parser.add_argument("meeting", help="Meeting to add users to")
    parser.add_argument("csv_file", help="CSV file to read")
    args = parser.parse_args()
    env = bootstrap(args.config_uri)
    root = env['root']
    print "Adding to meeting %r" % args.meeting
    #Just to make sure path exists
    meeting = root[args.meeting]
    pns = IParticipantNumbers(meeting)
    with open(args.csv_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=str(";"))
        for row in csv_reader:
            i = int(row[0])
            token = row[1]
            ticket = ParticipantNumberTicket(i, token, 'admin')
            pns.tickets[i] = ticket
            pns.token_to_number[token] = i
    print "-"*80
    print "Commit"
    transaction.commit()

if __name__ == '__main__':
    main()
