from api.routes import vacancies, vacancies_filters

routers = [
    vacancies.router,
    vacancies_filters.router,
]
