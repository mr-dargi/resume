from django.contrib.auth.models import BaseUserManager


class UserManger(BaseUserManager):
    def create_user(self, user_name, email, full_name, phone_nember, password):
        """
        Creates and saves a User with the given email, user_name, 
        full_name, phone_number and password.
        """
        if not user_name:
            raise ValueError("ایمیل خود را وارد نکرده اید")
        
        if not email:
            raise ValueError("ایمیل خود را وارد نکرده اید")

        if not full_name:
            raise ValueError("نام و نام خانوادگی خود را وارد نکرده اید")
        
        user = self.model(
            user_name=user_name,
            email=email,
            full_name=full_name,
            phone_nember=phone_nember
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, email, full_name, phone_nember, password):
        """
        Creates and saves a superuser with the given email, user_name, 
        full_name, phone_number and password.
        """
        user = self.create_user(
            user_name=user_name,
            email=email,
            full_name=full_name,
            phone_nember=phone_nember,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user