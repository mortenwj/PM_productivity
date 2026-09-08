export function downloadTextFile(filename: string, content: string, mimeType = 'text/plain'): void {
  const blob = new Blob([content], { type: `${mimeType};charset=utf-8` })
  const url = URL.createObjectURL(blob)
  const anchor = document.createElement('a')
  anchor.href = url
  anchor.download = filename
  anchor.click()
  URL.revokeObjectURL(url)
}

export function downloadWorkUnitPair(basename: string, wu: string, xaml: string): void {
  downloadTextFile(`${basename}.wu`, wu, 'application/xml')
  // Brief delay so browsers register both downloads.
  window.setTimeout(() => {
    downloadTextFile(`${basename}.xaml`, xaml, 'application/xml')
  }, 200)
}
