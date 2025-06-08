import type { FC } from 'react'
import { Chart } from 'react-chartjs-2'
import type { ChartData } from 'chart.js'
import type { BoxPlotDataPoint } from '@sgratzl/chartjs-chart-boxplot'

import styles from './SampleGraph.module.css'

type SampleGraphProps = {
	data: ChartData<'boxplot', BoxPlotDataPoint[], string>
}

export const SampleGraph: FC<SampleGraphProps> = ({ data }) => {
	const options = {
		responsive: true,
		maintainAspectRatio: false,
		plugins: {
			legend: {
				display: false
			}
		},
		scales: {
			y: {
				beginAtZero: true,
				ticks: {
					stepSize: 1,
				},
				title: {
					display: true,
					text: 'Значения',
				},
			},
			x: {
				title: {
					display: true,
					text: 'Категории',
				},
			},
		},
	} as any

	return (
		<div className={styles.root}>
			{data && <Chart key={JSON.stringify(data)} type='boxplot' data={data} options={options} />}
		</div>
	)
}
