
import html2pdf from 'html2pdf.js'
import styles from './Dashboard.module.css'
import { Report } from './components/Report/Report'
import { Card } from '../../components/Card/Card'
import { Header } from '../../components/Header/Header'
import { Filter, FilterGroup } from '../../components/FilterGroup/FilterGroup'
import { useSpecializations } from '../../hooks/filterLabels/useSpecializations'
import { useVacancyCounter } from '../../hooks/useVacancyCounter'
import { useSummaryLLM } from '../../hooks/useSummaryLLM'
import { useSalaryBoxplot } from '../../hooks/useSalaryBoxplot'
import { useSalaryBins } from '../../hooks/useSalaryBins'
import { useMemo, useState } from 'react'
import { useRegions } from '../../hooks/filterLabels/useRegions'
import { useGenders } from '../../hooks/filterLabels/useGenders'
import { useRadar } from '../../hooks/useRadar'
import { useResumeCounter } from '../../hooks/useResumeCounter'

const Dashboard = () => {
	document.getElementById('downloadBtn')?.addEventListener('click', () => {
		const element = document.body
		const opt = {
			margin: 0.5,
			filename: 'страница.pdf',
			image: { type: 'jpeg', quality: 0.98 },
			html2canvas: { scale: 2 },
			jsPDF: { unit: 'in', format: 'a4', orientation: 'landscape' },
		}
		html2pdf().set(opt).from(element).save()
	})

	const [reloader, setReloader] = useState<boolean>()

	const { specializations } = useSpecializations()
	const { regions } = useRegions()
	const { genders } = useGenders()

	const [filters, setFilters] = useState({
		specialization: [] as string[],
		region: [] as string[],
		gender: [] as string[],
	})

	const toggleFilterValue = (key: keyof typeof filters, value: string) => {
		setFilters((prev) => {
			const current = prev[key] as string[]
			const updated = current.includes(value)
				? current.filter((v) => v !== value)
				: [...current, value]

			return { ...prev, [key]: updated }
		})
	}

	const query = useMemo(() => {
		const params = new URLSearchParams()

		Object.entries(filters).forEach(([key, value]) => {
			if (Array.isArray(value)) {
				value.forEach((v) => params.append(key, v))
			} else {
				params.append(key, String(value))
			}
		})

		return params.toString()
	}, [reloader])

	const { vacancyCounter } = useVacancyCounter({ query })
	const { resumeCounter } = useResumeCounter({ query })
	const { summaryLLM } = useSummaryLLM({ query })
	const { salaryBoxplot } = useSalaryBoxplot({ query })
	const { salaryBins } = useSalaryBins({ query })
	const { radar } = useRadar({ query })

	return (
		<>
			<Header />

			<div className={styles.root}>
				<Report
					vacancyCounter={vacancyCounter}
					resumeCounter={resumeCounter}
					summaryLLM={summaryLLM}
					salaryBoxplot={salaryBoxplot}
					salaryBins={salaryBins}
					radar={radar}
				/>

				<Card className={styles.filtersCard}>
					<h2 className={styles.filtersTitle}>{'Фильтры'}</h2>

					<FilterGroup title={'Специализация'}>
						{specializations.map((item) => (
							<Filter
								label={item}
								checked={filters.specialization.includes(item)}
								onChange={() => toggleFilterValue('specialization', item)}
							/>
						))}
					</FilterGroup>

					<FilterGroup title={'Регион'}>
						{regions.map((item) => (
							<Filter
								label={item}
								checked={filters.region.includes(item)}
								onChange={() => toggleFilterValue('region', item)}
							/>
						))}
					</FilterGroup>

					<FilterGroup title={'Пол'}>
						{genders.map((item) => (
							<Filter
								label={item}
								checked={filters.gender.includes(item)}
								onChange={() => toggleFilterValue('gender', item)}
							/>
						))}
					</FilterGroup>

					<div className={styles.buttons}>
						<button
							onClick={() => setReloader(!reloader)}
							className={styles.filtersButton}
						>
							{'Обновить'}
						</button>

						<button
							id='downloadBtn'
							onClick={() => {}}
							className={styles.downloadButton}
						>
							{'Скачать в pdf'}
						</button>
					</div>
				</Card>
			</div>

			<div className={styles.dorateam} />
		</>
	)
}

export default Dashboard
