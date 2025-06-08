import type { FC } from 'react'

import styles from './Checkbox.module.css'

interface CheckboxProps {
	checked: boolean
	onChange: (checked: boolean) => void
  label?: string
}

export const Checkbox: FC<CheckboxProps> = ({ checked, onChange, label }) => {
	return (
		<label className={styles.checkbox}>
			<input
				type='checkbox'
				checked={checked}
				onChange={(e) => onChange(e.target.checked)}
			/>
			<span className={styles.checkmark}>
        {checked && <div className={styles.checkmarkIcon} />}
      </span>
      {label && <span className={styles.label}>{label}</span>}
		</label>
	)
}
