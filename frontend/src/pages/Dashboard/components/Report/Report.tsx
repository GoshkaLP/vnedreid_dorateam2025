import { useState, type FC } from 'react'

import styles from './Report.module.css'
import { Card } from '../../../../components/Card/Card'
import classNames from 'classnames'
import { Counter } from '../../../../components/Counter/Counter'
import ReactMarkdown from 'react-markdown'
import { GraphBox } from '../../../../components/GraphBox/GraphBox'
import { SampleGraph } from '../../../../components/SampleGraph/SampleGraph'
import { BarChart } from '../../../../components/BarChart/BarChart'
import { Radar } from '../../../../components/Radar/Radar'

type ReportProps = {
	vacancyCounter: {
		title: string
		value: number
	}
	resumeCounter: {
		title: string
		value: number
	}
	summaryLLM: {
		response: string | undefined
	}
	salaryBoxplot: {
		title: string
		data: {
			labels: string[]
			datasets: {
				label: string
				data: {
					min: number
					q1: number
					median: number
					mean: number
					q3: number
					max: number
				}[]
			}[]
		}
	}
	salaryBins: {
		title: string
		data: {
			labels: string[]
			datasets: {
				label: string
				data: number[]
				backgroundColor: string
				borderColor: string
				borderWidth: number
			}[]
		}
	}
	radar: {
		title: string
		data: {
			labels: string[]
			datasets: {
				label: string
				data: number[]
				backgroundColor?: string
				borderColor?: string
				pointBackgroundColor?: string
			}[]
		}
	}
}

export const Report: FC<ReportProps> = ({
	vacancyCounter,
	resumeCounter,
	summaryLLM,
	salaryBoxplot,
	salaryBins,
	radar,
}) => {
	const [page, setPage] = useState<'main' | 'map'>('main')

	return (
		<Card>
			<div className={styles.header}>
				<h1 className={styles.title}>{'Отчет'}</h1>

				<div className={styles.tabs}>
					<p
						className={classNames(
							styles.tab,
							page === 'main' && styles.tabActive
						)}
						onClick={() => setPage('main')}
					>
						{'Общая аналитика'}
					</p>
					<div className={styles.divider} />
					<p
						className={classNames(
							styles.tab,
							page === 'map' && styles.tabActive
						)}
						onClick={() => setPage('map')}
					>
						{'Бенефиты'}
					</p>
				</div>
			</div>

			<div className={styles.content}>
				<div className={styles.about}>
					<div className={styles.counters}>
						<Counter
							title={vacancyCounter.title}
							value={vacancyCounter.value}
						/>

						<Counter title={resumeCounter.title} value={resumeCounter.value} />
					</div>

					{page === 'main' && (
						<ReactMarkdown>{summaryLLM.response}</ReactMarkdown>
					)}
				</div>

				{page === 'main' && (
					<GraphBox title={salaryBins.title} hint={'Подробнее'}>
						<BarChart data={salaryBins.data} />
					</GraphBox>
				)}

				{page === 'main' && (
					<GraphBox title={salaryBoxplot.title} hint={'Подробнее'}>
						<SampleGraph data={salaryBoxplot.data} />
					</GraphBox>
				)}

				{page === 'map' && (
					<GraphBox title={'Статистика бенефитов'} hint={'Подробнее'}>
						<Radar data={radar.data} />
					</GraphBox>
				)}
			</div>
		</Card>
	)
}
