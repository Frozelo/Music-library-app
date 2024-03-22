@method_decorator(csrf_protect, name='dispatch')
class LastFmSearchView(View):
    # Этот класс не может быть использован напрямую, он предназначен только для наследования.
    def get_context_data(self, **kwargs):
        """Получить контекст для рендеринга шаблона."""
        context = {}
        # Определяем логику для общего контекста, если она есть
        return context

    def handle_last_fm_error(self, e):
        """Обработать возможные ошибки при работе с Last.fm API."""
        if isinstance(e, KeyError):
            return f"Missing data in response: {e}"
        return f"An error occurred: {e}"