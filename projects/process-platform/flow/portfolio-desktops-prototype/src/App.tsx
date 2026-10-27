import { useState } from 'react'
import { AppShell } from './components/AppShell'
import { CaseDetailScreen } from './screens/CaseDetailScreen'
import { PortfolioScreen } from './screens/PortfolioScreen'
import { ReportingScreen } from './screens/ReportingScreen'
import { WorklistScreen } from './screens/WorklistScreen'
import type { ScreenId } from './types/portfolio'

function App() {
  const [screen, setScreen] = useState<ScreenId>('worklist')
  const [selectedCaseId, setSelectedCaseId] = useState<string | null>(null)
  const [returnScreen, setReturnScreen] = useState<ScreenId>('worklist')

  function openCase(caseId: string) {
    setReturnScreen(screen === 'case-detail' ? returnScreen : screen)
    setSelectedCaseId(caseId)
    setScreen('case-detail')
  }

  function goBack() {
    setScreen(returnScreen)
    setSelectedCaseId(null)
  }

  function navigate(next: ScreenId) {
    setScreen(next)
    setSelectedCaseId(null)
  }

  return (
    <AppShell activeScreen={screen} onNavigate={navigate}>
      {screen === 'worklist' && <WorklistScreen onOpenCase={openCase} />}
      {screen === 'portfolio' && <PortfolioScreen onOpenCase={openCase} />}
      {screen === 'reporting' && <ReportingScreen />}
      {screen === 'case-detail' && selectedCaseId && (
        <CaseDetailScreen caseId={selectedCaseId} onBack={goBack} />
      )}
    </AppShell>
  )
}

export default App
