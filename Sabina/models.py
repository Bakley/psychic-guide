from django.db import models


class Sender(models.Model):
    """Here contains the Sender Details."""

    # parcel_id = models
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.PositiveIntegerField()
    address = models.IntegerField()
    national_id = models.IntegerField()

    def __str__(self):
        """The string represenation in the admin panel for the Sender details.

        Should showcase the Senders First name.
        """
        return self.first_name


class Receiver(models.Model):
    """Here contains the Receiver Details."""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.PositiveIntegerField()
    address = models.IntegerField()
    national_id = models.IntegerField()

    def __str__(self):
        """The string represenation in the admin panel for the Receiver details.

        Should showcase the Receiver First name.
        """
        return self.first_name


class Parcel(models.Model):
    """Here contains the Pracel Details."""

    parcel_id = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    destination_address = models.PositiveIntegerField()
    sender_details = models.ForeignKey(Sender, on_delete=models.CASCADE)
    receiver_details = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        """The string represenation in the admin panel for the parcel details.

        Should showcase the Parcel Id number.
        """
        return self.parcel_id
