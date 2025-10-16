from rest_framework import permissions
class AdminOrReadOnlyPermissions(permissions.IsAdminUser):

# has permission method overall project mai lg jai gi
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS: # get methods ko SAFE_METHODS khty hyn
      return True
    else:
      # Jo request kr rha hy user wo or admin same hon
      return bool(request.user and request.user.is_staff)
    

class ReviewUserOrReadyOnlyPermissions(permissions.BasePermission):
  # particular object pr permission lgany ky liy has_object_permission 

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return obj.apiuser == request.user  

class AdminOrReadOnlyPermission(permissions.IsAdminUser):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    else:
      return bool(request.user and request.user.is_staff)


    



       