class DrugPermission:
    def has_permission(self, request, view):
        if request.user.role in ["admin"]:
            return True

        if request.method == "GET":
            if request.user.role == "customer":
                return True

        return False
