import { useEffect, useState } from 'react'

type SpecializationsResponse = {
  specialization: string
}[]

export const useSpecializations = () => {
  const [data, setData] = useState<SpecializationsResponse>()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://10.10.162.1:8080/api/vacancies/filters/specializations')
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch count')
        return res.json()
      })
      .then((data) => setData(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  const specializations = data ? data.map((item) => item.specialization) : []

  return { specializations, loading }
}
