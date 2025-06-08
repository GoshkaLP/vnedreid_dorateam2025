import { type FC, type ReactNode } from 'react'

import styles from './FilterGroup.module.css'
import classNames from 'classnames'
import { Checkbox } from '../Checkbox/Checkbox'

interface FilterGroupProps {
	title: string
	children: ReactNode
	className?: string
}

export const FilterGroup: FC<FilterGroupProps> = ({
	title,
	children,
	className,
}) => {
	return (
		<div className={classNames(styles.rootgroup, className)}>
			<h2 className={styles.title}>{title}</h2>

			<div className={styles.items}>{children}</div>
		</div>
	)
}

interface FilterProps {
	label: string
	checked: boolean
	onChange: () => void
}

export const Filter: FC<FilterProps> = ({ checked, label, onChange }) => {
		return (
		<div className={styles.root}>
			<Checkbox checked={checked} onChange={onChange} label={label} />
		</div>
	)
}
