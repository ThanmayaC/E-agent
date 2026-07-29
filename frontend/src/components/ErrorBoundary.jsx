// A route-level error boundary: if a page throws while rendering, the shell
// (sidebar, header) survives and the content area shows a recoverable message
// instead of the whole app unmounting to a blank screen.
import { Component } from 'react'

export default class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { error: null }
  }

  static getDerivedStateFromError(error) {
    return { error }
  }

  componentDidCatch(error, info) {
    // Keep the detail in the console for debugging; the UI stays calm.
    console.error('Page error:', error, info)
  }

  componentDidUpdate(prevProps) {
    // Recover automatically when the user navigates to a different route.
    if (prevProps.routeKey !== this.props.routeKey && this.state.error) {
      this.setState({ error: null })
    }
  }

  render() {
    if (this.state.error) {
      return (
        <div className="card-pad max-w-xl">
          <div className="text-sm font-semibold text-rose-400">This page hit an error</div>
          <div className="text-sm text-slate-400 mt-2">
            {String(this.state.error?.message || this.state.error)}
          </div>
          <button className="btn mt-4" onClick={() => this.setState({ error: null })}>
            Try again
          </button>
        </div>
      )
    }
    return this.props.children
  }
}
