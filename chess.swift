// ... (previous code)

struct ChessboardView: View {
    // ... (previous code)

    private var lastMove: (fromRow: Int, fromCol: Int, toRow: Int, toCol: Int)? = nil

    // ... (previous code)

    private func performMove(_ move: (Int, Int, Int, Int)) {
        let (fromRow, fromCol, toRow, toCol) = move
        let selectedPiece = board[fromRow][fromCol]

        // Handle special moves
        switch selectedPiece {
        case .pawnW, .pawnB:
            handlePawnMove(fromRow, fromCol, toRow, toCol)
        case .kingW, .kingB:
            handleKingMove(fromRow, fromCol, toRow, toCol)
        default:
            break
        }

        board[toRow][toCol] = board[fromRow][fromCol]
        board[fromRow][fromCol] = .empty

        // Update last move
        lastMove = (fromRow, fromCol, toRow, toCol)
    }

    // ... (previous code)

    private func handlePawnMove(_ fromRow: Int, _ fromCol: Int, _ toRow: Int, _ toCol: Int) {
        let direction = (currentPlayer == .white) ? -1 : 1

        // Normal move
        if fromCol == toCol && board[toRow][toCol] == .empty {
            if fromRow + direction == toRow {
                // Check for en passant opportunity
                if let lastMove = lastMove, let piece = board[lastMove.toRow][lastMove.toCol] {
                    let enPassantRow = (currentPlayer == .white) ? 3 : 4
                    if lastMove.toRow == enPassantRow && lastMove.toCol == toCol &&
                        lastMove.fromRow == enPassantRow + direction && piece == .pawnB {
                        // Capture the pawn en passant
                        board[lastMove.toRow][lastMove.toCol] = .empty
                    }
                }
                return
            }
            // Initial two-square move
            if fromRow + 2 * direction == toRow && fromRow == (currentPlayer == .white ? 6 : 1) {
                return
            }
        }

        // Capture
        if abs(fromCol - toCol) == 1 && fromRow + direction == toRow {
            // Check for en passant opportunity
            if let lastMove = lastMove, let piece = board[lastMove.toRow][lastMove.toCol] {
                let enPassantRow = (currentPlayer == .white) ? 3 : 4
                if lastMove.toRow == enPassantRow && lastMove.toCol == toCol &&
                    lastMove.fromRow == enPassantRow + direction && piece == .pawnB {
                    // Capture the pawn en passant
                    board[lastMove.toRow][lastMove.toCol] = .empty
                }
            }
            return
        }
    }

    private func handleKingMove(_ fromRow: Int, _ fromCol: Int, _ toRow: Int, _ toCol: Int) {
        let kingSideCastleCol = 6
        let queenSideCastleCol = 2

        if fromRow == toRow && fromCol == 4 {
            if toCol == kingSideCastleCol {
                // King-side castling
                if canCastleKingSide() {
                    board[toRow][toCol - 1] = board[toRow][kingSideCastleCol]
                    board[toRow][kingSideCastleCol] = .empty
                }
            } else if toCol == queenSideCastleCol {
                // Queen-side castling
                if canCastleQueenSide() {
                    board[toRow][toCol + 1] = board[toRow][queenSideCastleCol]
                    board[toRow][queenSideCastleCol] = .empty
                }
            }
        }
    }

    private func canCastleKingSide() -> Bool {
        // Check conditions for king-side castling
        let kingRow = (currentPlayer == .white) ? 7 : 0
        return !hasMoved(kingRow, 4) &&
            !hasMoved(kingRow, 7) &&
            isEmpty(kingRow, 5) &&
            isEmpty(kingRow, 6) &&
            !isUnderAttack(kingRow, 4) &&
            !isUnderAttack(kingRow, 5) &&
            !isUnderAttack(kingRow, 6)
    }

    private func canCastleQueenSide() -> Bool {
        // Check conditions for queen-side castling
        let kingRow = (currentPlayer == .white) ? 7 : 0
        return !hasMoved(kingRow, 4) &&
            !hasMoved(kingRow, 0) &&
            isEmpty(kingRow, 1) &&
            isEmpty(kingRow, 2) &&
            isEmpty(kingRow, 3) &&
            !isUnderAttack(kingRow, 4) &&
            !isUnderAttack(kingRow, 3) &&
            !isUnderAttack(kingRow, 2)
    }

    private func hasMoved(_ row: Int, _ col: Int) -> Bool {
        // Check if the piece at the specified position has moved
        let piece = board[row][col]
        switch piece {
        case .rookW, .rookB, .kingW, .kingB:
            return false  // Add logic to track piece movements
        default:
            return true
        }
    }

    private func isEmpty(_ row: Int, _ col: Int) -> Bool {
        // Check if the specified square is empty
        return board[row][col] == .empty
    }

    private func isUnderAttack(_ row: Int, _ col: Int) -> Bool {
        // Check if the specified square is under attack by the opponent
        // Implement this based on your chess engine or logic
        return false
    }
}

struct ContentView: View {
    var body: some View {
        VStack {
            ChessboardView()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

@main
struct ChessApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
