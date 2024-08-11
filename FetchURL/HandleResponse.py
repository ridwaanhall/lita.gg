class HandleResponsePiS:
    @staticmethod
    def handle_data_func(data):
        if 'data' in data and 'rows' in data['data']:
            if len(data['data']['rows']) > 0:
                return data
            else:
                return {'status': '1', 'msg': 'Data not available.', 'data': {}}
        else:
            return {'status': '1', 'msg': 'Error occurred while fetching data.', 'data': {}}
