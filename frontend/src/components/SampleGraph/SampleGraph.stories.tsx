import type { Meta, StoryObj } from '@storybook/react-vite'

import { SampleGraph } from './SampleGraph'

const meta = {
	title: 'Graphs/SampleGraph',
	component: SampleGraph,
} satisfies Meta<typeof SampleGraph>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
		data: {
			labels: ['A', 'B', 'C'],
			datasets: [
				{
					label: 'Boxplot',
					data: [
						{ min: 1, q1: 2, median: 3, mean: 3.2, q3: 4, max: 5 },
						{ min: 2, q1: 3, median: 4, mean: 4, q3: 5, max: 6 },
						{ min: 0, q1: 1, median: 2, mean: 2, q3: 3, max: 4 },
					],
					backgroundColor: 'rgba(16, 155, 71, 0.3)',
					borderColor: '#109B47',
					borderWidth: 1.5,

					medianColor: '#0B7033',
					medianWidth: 2,

					whiskerColor: '#109B47',
					whiskerWidth: 1,

					outlierColor: '#79C197',
					itemRadius: 3,
				} as any,
			],
		},
	},
}
