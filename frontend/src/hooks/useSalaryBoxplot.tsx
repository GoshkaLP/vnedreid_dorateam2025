import { useEffect, useState } from 'react'

type SalaryBoxplotResponse = {
	vacancy: string
	min_salary: number
	q1_salary: number
	median_salary: number
	mean_salary: number
	q3_salary: number
	max_salary: number
}

export const useSalaryBoxplot = ({query} : {query?: string}) => {
	const [data, setData] = useState<SalaryBoxplotResponse>()
	const [loading, setLoading] = useState(true)

	useEffect(() => {
		fetch(`http://10.10.162.1:8080/api/vacancies/salary_stats?${query}`)
			.then((res) => {
				if (!res.ok) throw new Error('Failed to fetch salary_stats')
				return res.json()
			})
			.then((data) => setData(data))
			.catch(console.error)
			.finally(() => setLoading(false))
	}, [query])

	const salaryBoxplot = {
		title: 'Детальные метрики распределения зарпалат',
		data: {
			labels: Array(''),
			datasets: Array({
				label: '',
				data: data
					? [
							{
								min: data.min_salary,
								q1: data.q1_salary,
								median: data.median_salary,
								mean: data.mean_salary,
								q3: data.q3_salary,
								max: data.max_salary,
							},
						]
					: [],
				backgroundColor: 'rgba(16, 155, 71, 0.3)',
				borderColor: '#109B47',
				borderWidth: 1.5,

				medianColor: '#0B7033',
				medianWidth: 2,

				whiskerColor: '#109B47',
				whiskerWidth: 1,

				outlierColor: '#79C197',
				itemRadius: 3,
			}),
		},
	}

	return { salaryBoxplot, loading }
}
