import { useState, type FC } from 'react'

import styles from './Report.module.css'
import { Card } from '../../../../components/Card/Card'
import classNames from 'classnames'
import { Counter } from '../../../../components/Counter/Counter'
import ReactMarkdown from 'react-markdown'
import { GraphBox } from '../../../../components/GraphBox/GraphBox'
import { SampleGraph } from '../../../../components/SampleGraph/SampleGraph'
import { BarChart } from '../../../../components/BarChart/BarChart'

type ReportProps = {
	vacancyCounter: {
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
}

export const Report: FC<ReportProps> = ({
	vacancyCounter,
	summaryLLM,
	salaryBoxplot,
	salaryBins,
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
						{'Карта'}
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
						<Counter title={'-'} value={0} />
					</div>

					<ReactMarkdown>{summaryLLM.response}</ReactMarkdown>
				</div>

				<GraphBox title={salaryBins.title} hint={'Подробнее'}>
					<BarChart data={salaryBins.data} />
				</GraphBox>

				<GraphBox title={salaryBoxplot.title} hint={'Подробнее'}>
					<SampleGraph
						data={salaryBoxplot.data}
					/>
				</GraphBox>
			</div>
		</Card>
	)
}
