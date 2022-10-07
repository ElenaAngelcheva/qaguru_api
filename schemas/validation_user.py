from voluptuous import Schema, PREVENT_EXTRA

schema = Schema({
    'data':
        {
            'avatar': str,
            'email': str,
            'first_name': str,
            'id': int,
            'last_name': str},
    'support':
        {
            'text': str,
            'url': str}
},
    extra=PREVENT_EXTRA,
    required=True
)