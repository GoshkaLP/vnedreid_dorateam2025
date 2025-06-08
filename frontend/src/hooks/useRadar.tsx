import { useEffect, useState } from 'react'

type RadarResponse = {
	company: string
	benifits: number[]
}[]

export const useRadar = ({ query }: { query?: string }) => {
	const [data, setData] = useState<RadarResponse>()
	const [loading, setLoading] = useState(true)

	useEffect(() => {
		fetch(`http://10.10.162.1:8080/api/benifits/radar?${query}`)
			.then((res) => {
				if (!res.ok) throw new Error('Failed to fetch salary_bins')
				return res.json()
			})
			.then((data) => setData(data))
			.catch(console.error)
			.finally(() => setLoading(false))
	}, [query])

	const radar = {
		title: 'Статистика бенефитов',
		data: {
			labels: ['Страховка', 'Питание', 'Спорт', 'Гибкое расписание', 'Обучение'],
			datasets:
				data
					?.map((company) => {
						if (company.company === 'СДЭК') {
							return {
								label: company.company,
								data: company.benifits,
								backgroundColor: 'rgba(16, 155, 71, 0.3)',
								borderColor: '#109B47',
								pointBackgroundColor: '#109B47',
							}
						} else {
							return {
								label: company.company,
								data: company.benifits,
								backgroundColor: 'rgba(128, 128, 128, 0.2)',
								borderColor: '#808080',
								pointBackgroundColor: '#808080',
								hidden: true,
							}
						}
					})
					.sort((a, b) => {
						if (a.label === 'СДЭК') return -1
						if (b.label === 'СДЭК') return 1
						return a.label.localeCompare(b.label)
					}) ?? []
		},
	}

	return { radar, loading }
}
