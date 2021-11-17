from common import gmail_authenticate, search_messages


def mark_as_read(service, query):
    messages_to_mark = search_messages(service, query)
    return service.users().messages().batchModify(
      userId='me',
      body={
          'ids': [ msg['id'] for msg in messages_to_mark ],
          'removeLabelIds': ['UNREAD']
      }
    ).execute()


def mark_as_unread(service, query):
    messages_to_mark = search_messages(service, query)
    return service.users().messages().batchModify(
        userId='me',
        body={
            'ids': [ msg['id'] for msg in messages_to_mark ],
            'addLabelIds': ['UNREAD']
        }
    ).execute()


if __name__ == "__main__":
    service = gmail_authenticate()
    query = "This is my first title"

    # mark_as_read(service, query)
    # mark_as_unread(service, query)
