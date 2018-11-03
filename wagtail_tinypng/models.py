"""Custom Image Models."""
from django.db import models

from wagtail.images.models import Image, AbstractImage, AbstractRendition


class CustomImage(AbstractImage):
    """New custom wagtail image model. Supports caption and tinified boolean."""

    caption = models.CharField(max_length=255, blank=True)
    tinified = models.BooleanField(default=False, db_index=True)

    admin_form_fields = Image.admin_form_fields + (
        'caption',
    )

    @property
    def default_alt_text(self):
        """Better alt text."""
        return self.caption if self.caption else self.title


class CustomRendition(AbstractRendition):
    """Custom wagtail rendition model."""

    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        """Meta data."""

        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
