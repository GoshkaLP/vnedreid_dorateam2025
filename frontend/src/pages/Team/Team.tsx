import { useNavigate } from 'react-router-dom';
import styles from './Team.module.css'

const Team = () => {
	const navigate = useNavigate();

	return (
		<div className={styles.root}>
			<div className={styles.dorateam} onClick={() => navigate('/dashboard')} />
		</div>
	)
}

export default Team;