class InlineEditButtonMixin(object):
    """
    Allows adding edit button to Inline edit blocks including
    `TabularInline` and `StackedInline` classes.

    Example:
        class RelatedInline(EditButtonMixin, admin.TabularInline):
            model = RelatedModel

    Note:
        In case you specify custom `fields` list, you have to
        add `_edit` button manually.

            fields = ('name', '_edit')
    """

    def _edit(self, instance):
        from django.utils.safestring import mark_safe
        from django.core.urlresolvers import reverse
        from django.utils.translation import ugettext as _

        if instance.pk:
            html = '<a href="{href}" onclick="return showAddAnotherPopup(this);">{title}</a>'.format(
                href=reverse('admin:{model.app_label}_{model.model_name}_change'\
                            .format(model=self.model._meta), args=[instance.pk]),
                title=_('Edit')
            )
        else:
            html = _('Not saved')
        return mark_safe('<div style="width: 100%%; text-align: center;">%s</div>' % html)
    _edit.short_description = ''

    def get_readonly_fields(self, request, obj=None):
        if not '_edit' in self.readonly_fields:
            return self.readonly_fields + ('_edit',)
