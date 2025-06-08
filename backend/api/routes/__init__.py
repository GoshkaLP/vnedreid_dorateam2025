from api.routes import radar, resume, vacancies, vacancies_filters

routers = [
    vacancies.router,
    vacancies_filters.router,
    resume.router,
    radar.router,
]
