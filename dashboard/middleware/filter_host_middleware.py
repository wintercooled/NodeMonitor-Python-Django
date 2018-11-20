from django.http import HttpResponseForbidden

class FilterHostMiddleware(object):

    def process_request(self, request):

        allowed_hosts = ['127.0.0.1', 'localhost']  # specify complete host names here
        host = request.META.get('HTTP_HOST')

        if host[:7] == '192.168':  # if the host starts with 192.168 then add to the allowed hosts
            allowed_hosts.append(host)

        if host not in allowed_hosts:
            raise HttpResponseForbidden

        return None