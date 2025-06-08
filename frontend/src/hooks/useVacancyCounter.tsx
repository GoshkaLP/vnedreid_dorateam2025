import { useEffect, useState } from 'react'

type VacancyCounterResponse = {
  count: number
}

export const useVacancyCounter = ({query} : {query?: string}) => {
  const [data, setData] = useState<VacancyCounterResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`http://10.10.162.1:8080/api/vacancies/count?${query}`)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch count')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [query])

  const vacancyCounter = {
    title: 'Всего вакансий',
    value: data?.count ?? 0,
  }

  return { vacancyCounter, loading }
}
