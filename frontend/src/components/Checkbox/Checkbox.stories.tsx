import type { Meta, StoryObj } from '@storybook/react-vite'

import { Checkbox } from './Checkbox'

const meta = {
	title: 'Main/Checkbox',
	component: Checkbox,
} satisfies Meta<typeof Checkbox>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
	args: {
    checked: false,
    onChange: () => {}
  },
}

export const Checked: Story = {
	args: {
    checked: true,
    onChange: () => {}
  },
}

export const WithLabel: Story = {
	args: {
    checked: true,
    onChange: () => {},
    label: 'Курьер'
  },
}
