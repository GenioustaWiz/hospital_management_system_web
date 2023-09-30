from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Visit
from django.utils import timezone
from datetime import timedelta

def record_visit(request):
    if request.method == 'POST':
        ip_address = request.META.get('REMOTE_ADDR')

        # Define the threshold for session expiration (e.g., 30 minutes)
        session_expiration_threshold = timedelta(minutes=30)

        try:
            # Retrieve the previous visit for the IP address
            previous_visit = Visit.objects.get(ip_address=ip_address)

            # Check if the previous visit is still within the session expiration threshold
            time_since_last_visit = timezone.now() - previous_visit.last_visit
            if time_since_last_visit >= session_expiration_threshold:
                # Increment the visit count if the session has expired
                previous_visit.increment_visit_count()
            else:
                # Session is still active
                return JsonResponse({'status': 'active_session'})
        except Visit.DoesNotExist:
            # If there is no previous visit, create a new one
            visit = Visit(ip_address=ip_address)
            visit.save()
            return JsonResponse({'status': 'success'})

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

# @csrf_exempt
# def record_visit(request):
#     if request.method == 'POST':
#         ip_address = request.META.get('REMOTE_ADDR')
#         visit, created = Visit.objects.get_or_create(ip_address=ip_address)

#         # Increment the visit count for the IP address
#         if not created:
#             visit.increment_visit_count()


#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})
