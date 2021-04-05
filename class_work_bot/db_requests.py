UPDATE_PHONE = '''
    UPDATE users
    SET phone = '{}'
    WHERE id = '{}'
'''

SELECT_CODE = '''
    SELECT stage
    FROM users
    WHERE id = '{}'
'''
