import type { FC, ReactNode } from 'react'

import styles from './Header.module.css'

interface HeaderProps {
  children?: ReactNode
}

export const Header: FC<HeaderProps> = ({ children }) => {
	return (
		<div className={styles.root}>
      <div className={styles.logo} />
      {children}
    </div>
	)
}
