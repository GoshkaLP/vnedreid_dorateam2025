import { useEffect, useState } from 'react'

type SalaryBinsResponse = {
  salary_range: string
  count: number
}[]

export const useSalaryBins = ({query} : {query?: string}) => {
  const [data, setData] = useState<SalaryBinsResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`http://10.10.162.1:8080/api/vacancies/salary_bins?${query}`)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch salary_bins')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [query])

  const salaryBins = {
    title: 'Распределение зарплат',
    data: {
		labels: data?.map((bin) => bin.salary_range) ?? [],
		datasets: [
			{
				label: 'Количество вакансий',
				data: data?.map((bin) => bin.count) ?? [],
				backgroundColor: 'rgba(16, 155, 71, 0.3)',
				borderColor: '#109B47',
				borderWidth: 1.5,
			},
		],
	}
  }

  return { salaryBins, loading }
}
