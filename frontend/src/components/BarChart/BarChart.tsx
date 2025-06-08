import type { FC } from 'react'
import { Chart } from 'react-chartjs-2'
import type { ChartData } from 'chart.js'
import type { ChartOptions } from 'chart.js'

import styles from './BarChart.module.css'

type BarChartProps = {
	data: ChartData<'bar', number[], string>
}

export const BarChart: FC<BarChartProps> = ({ data }) => {
	const options: ChartOptions<'bar'> = {
		responsive: true,
		maintainAspectRatio: false,
		plugins: {
			legend: {
				position: 'top',
				labels: {
					font: { size: 12 },
				},
			},
			title: {
				display: true,
				text: 'Bar Chart',
				font: {
					size: 16,
				},
			},
		},
		scales: {
			y: {
				beginAtZero: true,
				ticks: {
					stepSize: 10,
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
	}

	return (
		<div className={styles.root}>
			{data && <Chart type="bar" data={data} options={options} />}
		</div>
	)
}
