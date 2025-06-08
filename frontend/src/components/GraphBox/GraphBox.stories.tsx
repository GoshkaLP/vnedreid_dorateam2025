import type { Meta, StoryObj } from '@storybook/react-vite'

import { GraphBox } from './GraphBox'

const meta = {
	title: 'Main/GraphBox',
	component: GraphBox,
} satisfies Meta<typeof GraphBox>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
		title: 'Заголовок',
		hint: 'Подробнее',
		children: (
			<div
				style={{
					backgroundColor: '#B9B9B9',
					width: '100%',
					height: '200px',
					borderRadius: '16px',
				}}
			/>
		),
	},
}
